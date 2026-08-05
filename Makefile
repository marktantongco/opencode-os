.PHONY: audit fix matrix update-matrix generate-config check-config setup-hooks help

## audit — Check agent model assignments (silent on pass)
audit:
	python3 scripts/audit_agent_models.py --check

## fix — Apply matrix models to configs (auto-fix drift)
fix:
	python3 scripts/audit_agent_models.py --fix

## matrix — Regenerate MODEL_ASSIGNMENT_MATRIX.md from opencode.jsonc (full overwrite)
matrix:
	python3 scripts/audit_agent_models.py --generate-matrix

## update-matrix — Update auto-generated tables in matrix, preserve hand-written sections
update-matrix:
	python3 scripts/audit_agent_models.py --update-matrix

## generate-config — Regenerate opencode.jsonc from models.yaml
generate-config:
	python3 scripts/generate_config.py

## check-config — Verify opencode.jsonc matches models.yaml
check-config:
	python3 scripts/generate_config.py --check

## setup-hooks — Install shared pre-commit hook
setup-hooks:
	bash scripts/setup-hooks.sh

## help — Show available targets
help:
	@echo "Available targets:"
	@echo "  make audit            Check agent model assignments (silent on pass)"
	@echo "  make fix              Apply matrix models to configs (auto-fix drift)"
	@echo "  make matrix           Regenerate matrix from config (full overwrite)"
	@echo "  make update-matrix    Update tables in matrix, preserve hand-written sections"
	@echo "  make generate-config  Regenerate opencode.jsonc from models.yaml"
	@echo "  make check-config     Verify opencode.jsonc matches models.yaml"
	@echo "  make setup-hooks      Install shared pre-commit hook"
	@echo "  make help             Show this help"
