import json
import tempfile
import unittest
from pathlib import Path
from scripts.validate_connections import validate
from scripts.normalize_marketing_data import normalize
from scripts.calculate_health_score import calculate
from scripts.detect_anomalies import detect

ROOT = Path(__file__).resolve().parents[1]

class IntegrationTests(unittest.TestCase):
    def test_mock_connection_has_no_embedded_secret(self):
        data=json.loads((ROOT / "examples/multi-channel/mock-connection.json").read_text())
        self.assertEqual(validate(data), [])
    def test_embedded_token_is_rejected(self):
        data={"connection_id":"x","organization_id":"o","provider":"p","access_mode":"observe","status":"healthy","access_token":"secret"}
        self.assertTrue(any("forbidden" in e for e in validate(data)))
    def test_normalization_preserves_distinct_metrics(self):
        base={"organization_id":"o","project_id":"p","provider":"x","channel":"paid_search","date":"2026-07-01","value":2}
        self.assertEqual(normalize({**base,"metric":"conversions"})["metric_name"], "conversions")
        self.assertEqual(normalize({**base,"metric":"qualified_leads"})["metric_name"], "qualified_leads")
    def test_health_score_marks_insufficient_coverage(self):
        result=calculate({"scope_id":"p","minimum_coverage":.8,"dimensions":[{"name":"data","score":80,"weight":.2,"confidence":1,"available":True},{"name":"revenue","score":None,"weight":.8,"confidence":0,"available":False}]})
        self.assertEqual(result["band"], "insufficient_data")
        self.assertIsNone(result["score"])
    def test_anomaly_detector_flags_large_drop(self):
        result=detect({"scope_id":"p","metric_name":"leads","minimum_history":6,"z_threshold":2,"percent_threshold":.25,"series":[{"period":str(i),"value":v,"complete":True} for i,v in enumerate([40,42,41,43,39,42,12])]})
        self.assertIn(result["severity"], {"medium","high","critical"})

if __name__ == "__main__": unittest.main()
