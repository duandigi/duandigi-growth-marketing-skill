import unittest

from scripts.score_experiments import score_experiment


class ScoringTests(unittest.TestCase):
    def test_high_value_low_cost_scores_high(self):
        result = score_experiment({
            "impact": 9,
            "confidence": 9,
            "strategic_fit": 9,
            "reusability": 8,
            "revenue_relevance": 9,
            "effort": 2,
            "risk": 1,
        })
        self.assertGreaterEqual(result["priority_score"], 75)
        self.assertEqual(result["priority_band"], "high")

    def test_high_risk_reduces_score(self):
        base = {"impact": 8, "confidence": 7, "strategic_fit": 8, "reusability": 7, "revenue_relevance": 8, "effort": 5}
        low = score_experiment({**base, "risk": 2})["priority_score"]
        high = score_experiment({**base, "risk": 10})["priority_score"]
        self.assertGreater(low, high)

    def test_out_of_range_is_rejected(self):
        with self.assertRaises(ValueError):
            score_experiment({"impact": 11, "confidence": 5, "strategic_fit": 5, "reusability": 5, "revenue_relevance": 5, "effort": 5, "risk": 5})


if __name__ == "__main__":
    unittest.main()
