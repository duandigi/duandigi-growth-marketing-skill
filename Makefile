.PHONY: validate test catalog demo

validate:
	python3 scripts/validate_skills.py
	python3 -m unittest discover -s tests -v
	python3 scripts/build_catalog.py --check
	python3 scripts/validate_repository.py
	python3 scripts/validate_connections.py examples/multi-channel/mock-connection.json
	python3 scripts/mock_connector.py health examples/multi-channel/mock-connection.json >/dev/null
	python3 scripts/normalize_marketing_data.py examples/multi-channel/mock-provider-data.json >/dev/null
	python3 scripts/calculate_health_score.py examples/multi-channel/health-score-input.json >/dev/null
	python3 scripts/detect_anomalies.py examples/multi-channel/anomaly-input.json >/dev/null

test:
	python3 -m unittest discover -s tests -v

catalog:
	python3 scripts/build_catalog.py

demo:
	python3 scripts/mock_connector.py list-assets examples/multi-channel/mock-connection.json
	python3 scripts/calculate_health_score.py examples/multi-channel/health-score-input.json
	python3 scripts/detect_anomalies.py examples/multi-channel/anomaly-input.json
