HELM_VALUES_DIR = values

ROOT_DIR := $(shell git rev-parse --show-toplevel)
TEMP_DIR := $(shell mktemp -d)
HELM_VALUES := $(wildcard $(HELM_VALUES_DIR)/*.yaml)
ACCESS_TOKEN := $(shell gcloud auth print-access-token)
HELM_ARGS := $(foreach value,$(HELM_VALUES),-f $(value))

.PHONY: template
template:
	@helm template openapi $(ROOT_DIR)/chart/ $(HELM_ARGS)


.PHONY: generate
generate:
	openapi-python-client generate \
		--path "$(ROOT_DIR)/configs/openapi.yaml" \
		--config "$(ROOT_DIR)/configs/config.yaml" \
		--custom-template-path "$(ROOT_DIR)/templates/" \
		--output-path "$(TEMP_DIR)/" \
		--overwrite

	rsync -avh --progress --delete \
		"$(TEMP_DIR)/freshdesk/" "$(ROOT_DIR)/freshdesk/"

	cp -rf \
		"$(TEMP_DIR)/pyproject.toml" "$(TEMP_DIR)/README.md" "$(ROOT_DIR)/"

	rm -rf "$(TEMP_DIR)/"
