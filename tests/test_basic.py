from pathlib import Path
import os
import urllib.request
import ssl
import crowelab_pyir

def setup_function():
    os.environ["IGDATA"] = str(Path("pyir/data/germlines").absolute())


def teardown_function():
    if "IGDATA" in os.environ:
        del os.environ["IGDATA"]


def test_bcr():
    with open("tests/fixtures/IGHV.fasta", "w") as f:
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        with urllib.request.urlopen(
            "https://www.imgt.org/download/V-QUEST/IMGT_V-QUEST_reference_directory/Homo_sapiens/IG/IGHV.fasta",
            context=ssl_context
        ) as response:
            original_fasta = response.read().decode('utf-8')

        f.write(original_fasta.replace(".", ""))  # replace the gaps
        f.flush()
        all_seqs_output = crowelab_pyir.PyIR(
            query=f.name,
            args=[
                "--outfmt",
                "dict",
                "--receptor",
                "Ig",
                "--species",
                "human",
                "--input_type",
                "fasta",
                "--sequence_type",
                "nucl",
                "--silent",
            ],
        ).run()
        assert len(all_seqs_output.keys()) == original_fasta.count(">"), "Some sequences were not IgBlasted."



def test_tcr():
    with open("tests/fixtures/TRBV.fasta", "w") as f:
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        with urllib.request.urlopen(
            "https://www.imgt.org/download/V-QUEST/IMGT_V-QUEST_reference_directory/Homo_sapiens/TR/TRBV.fasta",
            context=ssl_context
        ) as response:
            original_fasta = response.read().decode('utf-8')

        f.write(original_fasta.replace(".", ""))  # replace the gaps
        f.flush()
        all_seqs_output = crowelab_pyir.PyIR(
            query=f.name,
            args=[
                "--outfmt",
                "dict",
                "--receptor",
                "TCR",
                "--species",
                "human",
                "--input_type",
                "fasta",
                "--sequence_type",
                "nucl",
                "--silent",
            ],
        ).run()
        assert len(all_seqs_output.keys()) == original_fasta.count(">"), "Some sequences were not IgBlasted."

        results = [
            {
                "expected_v_call": key.split("|")[1],
                "v_call": result["v_call"].split(",")[0],
                "fwr1_aa": result["fwr1_aa"],
                "cdr1_aa": result["cdr1_aa"],
                "fwr2_aa": result["fwr2_aa"],
                "cdr2_aa": result["cdr2_aa"],
                "fwr3_aa": result["fwr3_aa"],
            }
            for key, result in all_seqs_output.items()
        ]
        results = sorted(results, key=lambda x: x["expected_v_call"])

        trbv26_results = [r for r in results if r["v_call"] == "TRBV26*01"]
        if trbv26_results:
            assert trbv26_results[0]["cdr1_aa"] == "MNHVT"
            assert trbv26_results[0]["cdr2_aa"] == "SPGTGS"
