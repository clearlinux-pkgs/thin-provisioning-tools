PKG_NAME := thin-provisioning-tools
URL = https://github.com/jthornber/thin-provisioning-tools/archive/v1.0.13/thin-provisioning-tools-1.0.13.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/vendor/thin-provisioning-tools/snapshot/thin-provisioning-tools-2024-07-30-16-03-19.tar.xz ./vendor $(CGIT_BASE_URL)/vendor/thin-provisioning-tools/snapshot/thin-provisioning-tools-2025-01-02-23-41-04.tar.gz ./vendor

include ../common/Makefile.common
