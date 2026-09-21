#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/mediatek',
    'hardware/mediatek/libmtkperf_client',
    'hardware/xiaomi',
    'vendor/xiaomi/earth'
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    ('vendor.mediatek.hardware.videotelephony@1.0',): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    'system_ext/priv-app/ImsService/ImsService.apk': blob_fixup()
        .apktool_patch('blob-patches'),
    'system_ext/lib64/libimsma.so': blob_fixup()
        .replace_needed('libsink.so', 'libsink-mtk.so'),
    'system_ext/lib64/libsink-mtk.so': blob_fixup()
        .add_needed('libaudioclient_shim.so'),
    'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b': blob_fixup()
        .replace_needed('libavservices_minijail_vendor.so', 'libavservices_minijail.so')
        .replace_needed('libcodec2_hidl@1.0.so', 'libcodec2_hidl@1.0-v31.so')
        .replace_needed('libcodec2_hidl@1.1.so', 'libcodec2_hidl@1.1-v31.so')
        .replace_needed('libcodec2_hidl@1.2.so', 'libcodec2_hidl@1.2-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so'),
    'vendor/bin/mnld' : blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so')
        .replace_needed('libmnl.so', 'libmnl_mtk.so'),
    'vendor/lib64/hw/sensors.mediatek.V2.0.so': blob_fixup()
       .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
    'vendor/lib64/libcodec2_hidl@1.0-v31.so': blob_fixup()
        .replace_needed('libstagefright_bufferqueue_helper.so', 'libstagefright_bufferqueue_helper-v31.so')
        .replace_needed('libcodec2_hidl_plugin.so', 'libcodec2_hidl_plugin-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libui.so', 'libui-v34.so')
        .add_needed('libbase_shim.so'),
    'vendor/lib64/libcodec2_hidl@1.1-v31.so': blob_fixup()
        .replace_needed('libstagefright_bufferqueue_helper.so', 'libstagefright_bufferqueue_helper-v31.so')
        .replace_needed('libcodec2_hidl@1.0.so', 'libcodec2_hidl@1.0-v31.so')
        .replace_needed('libcodec2_hidl_plugin.so', 'libcodec2_hidl_plugin-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libui.so', 'libui-v34.so')
        .add_needed('libbase_shim.so'),
    'vendor/lib64/libcodec2_hidl@1.2-v31.so': blob_fixup()
        .replace_needed('libstagefright_bufferqueue_helper.so', 'libstagefright_bufferqueue_helper-v31.so')
        .replace_needed('libcodec2_hidl@1.0.so', 'libcodec2_hidl@1.0-v31.so')
        .replace_needed('libcodec2_hidl@1.1.so', 'libcodec2_hidl@1.1-v31.so')
        .replace_needed('libcodec2_hidl_plugin.so', 'libcodec2_hidl_plugin-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libui.so', 'libui-v34.so')
        .add_needed('libbase_shim.so'),
    'vendor/lib64/libcodec2_hidl_plugin-v31.so': blob_fixup()
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so'),
    ('vendor/lib64/libcodec2_mtk_c2store.so', 'vendor/lib64/libcodec2_vpp_qt_plugin.so', 'vendor/lib64/libcodec2_vpp_rs_plugin.so'): blob_fixup()
        .replace_needed('libcodec2_soft_common.so', 'libcodec2_soft_common-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so')
        .replace_needed('libsfplugin_ccodec_utils.so', 'libsfplugin_ccodec_utils-v31.so'),
    ('vendor/lib64/libcodec2_mtk_vdec.so', 'vendor/lib64/libcodec2_mtk_venc.so'): blob_fixup()
        .replace_needed('libcodec2_soft_common.so', 'libcodec2_soft_common-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libformatter.so', 'libformatter_mtk.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so')
        .replace_needed('libsfplugin_ccodec_utils.so', 'libsfplugin_ccodec_utils-v31.so')
        .replace_needed('libui.so', 'libui-v34.so'),
    'vendor/lib64/libcodec2_soft_common-v31.so': blob_fixup()
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so')
        .replace_needed('libsfplugin_ccodec_utils.so', 'libsfplugin_ccodec_utils-v31.so'),
    'vendor/lib64/libcodec2_vndk-v31.so': blob_fixup()
        .replace_needed('libui.so', 'libui-v34.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
    'vendor/lib64/libsfplugin_ccodec_utils-v31.so': blob_fixup()
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so'),
    ('vendor/bin/hw/android.hardware.gnss-service.mediatek', 'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so'): blob_fixup()
        .replace_needed('android.hardware.gnss-V1-ndk_platform.so', 'android.hardware.gnss-V1-ndk.so'),
    'vendor/bin/hw/mtkfusionrild' : blob_fixup()
        .add_needed('libutils-v32.so'),
    'vendor/bin/hw/vendor.mediatek.hardware.mtkpower@1.0-service': blob_fixup()
        .replace_needed('android.hardware.power-V2-ndk_platform.so', 'android.hardware.power-V2-ndk.so'),
    ('vendor/lib64/libaalservice.so', 'vendor/lib64/libcam.utils.sensorprovider.so'): blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),
    'vendor/etc/vintf/manifest/manifest_media_c2_V1_2_default.xml': blob_fixup()
        .regex_replace('1.1', '1.2'),
    'vendor/lib64/hw/vendor.mediatek.hardware.pq@2.15-impl.so': blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so')
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),
    'vendor/lib64/libmtkcam_featurepolicy.so': blob_fixup()
        .binary_regex_replace(b'\x34\xE8\x87\x40\xB9', b'\x34\x28\x02\x80\x52'),
    ('vendor/lib64/libmtkcam_stdutils.so', 'vendor/lib64/hw/android.hardware.camera.provider@2.6-impl-mediatek.so'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),
    'vendor/lib64/sensors.camera.light.so': blob_fixup()
        .replace_needed('libcamera2ndk_vendor.so', 'libcamera2ndk_vendor-v35.so'),
    ('vendor/lib64/libteei_daemon_vfs.so', 'vendor/lib64/lib3a.flash.so', 'vendor/lib64/libSQLiteModule_VER_ALL.so'): blob_fixup()
        .add_needed('liblog.so'),
    'vendor/lib64/libmnl_mtk.so' : blob_fixup()
        .add_needed('libcutils.so'),
    'vendor/lib/hw/audio.primary.mt6768.so' : blob_fixup()
        .add_needed('libstagefright_foundation-v33.so'),
    ('vendor/lib/libnvram.so', 'vendor/lib64/libnvram.so', 'vendor/lib64/libsysenv.so') : blob_fixup()
        .add_needed('libbase_shim.so'),
    'vendor/lib64/hw/hwcomposer.mt6768.so' : blob_fixup()
        .add_needed('libprocessgroup_shim.so'),
    (
        'vendor/lib/hw/audio.primary.mt6768.so',
        'vendor/lib/librt_extamp_intf.so',
        'vendor/lib64/hw/vendor.mediatek.hardware.pq@2.15-impl.so',
    ): blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'earth',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
