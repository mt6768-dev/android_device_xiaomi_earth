/*
 * Copyright (C) 2021 The LineageOS Project
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <libinit_variant.h>
#include <libinit_utils.h>
#include <unistd.h>

#include "vendor_init.h"

static const variant_info_t aether_info = {
    .hwc_value = "",
    .sku_value = "aether",

    .brand = "Redmi",
    .device = "aether",
    .marketname = "Redmi 12C",
    .model = "22126RN91Y",
    .build_fingerprint = "Redmi/aether_global/aether:14/UP1A.231005.007/V816.0.2.0.UCVMIXM:user/release-keys"
};

static const variant_info_t earth_info = {
    .hwc_value = "",
    .sku_value = "earth",

    .brand = "Redmi",
    .device = "earth",
    .marketname = "Redmi 12C",
    .model = "22120RN86G",
    .build_fingerprint = "Redmi/earth_global/earth:14/UP1A.231005.007/V816.0.2.0.UCVMIXM:user/release-keys"
};

static const variant_info_t earth_la_info = {
    .hwc_value = "",
    .sku_value = "earth_la",

    .brand = "Redmi",
    .device = "earth",
    .marketname = "Redmi 12C",
    .model = "2212ARNC4L",
    .build_fingerprint = "Redmi/earth_global/earth:14/UP1A.231005.007/V816.0.2.0.UCVMIXM:user/release-keys"
};

static const variant_info_t earth_p_info = {
    .hwc_value = "",
    .sku_value = "earth_p",

    .brand = "Poco",
    .device = "earth",
    .marketname = "POCO C55",
    .model = "22127PC95G",
    .build_fingerprint = "POCO/earth_p_global/earth:14/UP1A.231005.007/V816.0.2.0.UCVMIXM:user/release-keys"
};

static const std::vector<variant_info_t> variants = {
    aether_info,
    earth_info,
    earth_la_info,
    earth_p_info,
};

void vendor_load_properties() {
    if (access("/system/bin/recovery", F_OK) != 0) {
        search_variant(variants);
    }
}
