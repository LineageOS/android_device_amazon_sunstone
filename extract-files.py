#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

_displayservice_ping = (
    b'_ZN7lineage10frameworks14displayservice4V1_014IEventCallback4pingEv'
)
_displayservice_unresolved = (
    rb'_ZN7lineage10frameworks14displayservice4V1_01[45]I[A-Za-z0-9_]*'
    rb'(?:linkToDeath|unlinkToDeath|getDebugInfo|getHashChain|'
    rb'interfaceChain|interfaceDescriptor|5debug|registerForNotifications)'
    rb'[A-Za-z0-9_]*'
)

namespace_imports = [
    'device/amazon/sunstone',
    'hardware/amazon',
    'hardware/mediatek',
    'hardware/mediatek/libmtkperf_client',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    ('vendor/bin/hw/android.hardware.keymaster@4.0-service.optee', 'vendor/lib64/libkeymaster4-v30.so',
     'vendor/lib64/libkeymaster4support-v30.so', 'vendor/lib64/libkeymaster_messages-v30.so',
     'vendor/lib64/libkeymaster_portable-v30.so', 'vendor/lib64/libpuresoftkeymasterdevice-v30.so',
     'vendor/lib64/libsoft_attestation_cert-v30.so'): blob_fixup()
        .replace_needed('libkeymaster4.so', 'libkeymaster4-v30.so')
        .replace_needed('libkeymaster4support.so', 'libkeymaster4support-v30.so')
        .replace_needed('libkeymaster_messages.so', 'libkeymaster_messages-v30.so')
        .replace_needed('libkeymaster_portable.so', 'libkeymaster_portable-v30.so')
        .replace_needed('libpuresoftkeymasterdevice.so', 'libpuresoftkeymasterdevice-v30.so')
        .replace_needed('libsoft_attestation_cert.so', 'libsoft_attestation_cert-v30.so'),
    ('vendor/lib/android.hardware.audio.common-util-v30.so', 'vendor/lib/android.hardware.audio.common@6.0-util-v30.so',
     'vendor/lib/hw/audio.primary.mt8188.so', 'vendor/lib/hw/fireos.hardware.audio@6.0-impl.so',
     'vendor/lib/libasp.so', 'vendor/lib/libaudioprimarydevicehalifclient.so', 'vendor/lib/libedgeflow_core.so',
     'vendor/lib/libtensorflowlite_c-v30.so'): blob_fixup()
        .replace_needed('android.hardware.audio.common-util.so', 'android.hardware.audio.common-util-v30.so')
        .replace_needed('android.hardware.audio.common@6.0-util.so', 'android.hardware.audio.common@6.0-util-v30.so')
        .replace_needed('libmedia_helper.so', 'libmedia_helper-v30.so')
        .replace_needed('libtensorflowlite_c.so', 'libtensorflowlite_c-v30.so'),
    ('vendor/lib/hw/fireos.hardware.audio@6.0-impl.so', 'vendor/lib64/hw/android.hardware.camera.provider@2.6-impl-mediatek.so',
     'vendor/lib64/hw/vendor.mediatek.hardware.pq@2.6-impl.so',
     'vendor/lib64/libmtkcam_hal_android_app_cbadaptor.so'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),
    ('vendor/lib/libMtkOmxVdecEx.so', 'vendor/lib/libMtkOmxVenc.so'): blob_fixup()
        .replace_needed('libui.so', 'libui-v30.so'),
    ('vendor/lib/libh264enc_sa.ca7.so', 'vendor/lib/libmp4enc_sa.ca7.so', 'vendor/lib/libthha.so',
     'vendor/lib/libvc1dec_sa.ca7.so', 'vendor/lib/libvcodec_oal.so', 'vendor/lib/libvp8dec_sa.ca7.so',
     'vendor/lib/libvp9dec_sa.ca7.so'): blob_fixup()
        .clear_symbol_version('__aeabi_memclr')
        .clear_symbol_version('__aeabi_memclr4')
        .clear_symbol_version('__aeabi_memcpy')
        .clear_symbol_version('__aeabi_memcpy4')
        .clear_symbol_version('__aeabi_memmove')
        .clear_symbol_version('__aeabi_memset')
        .clear_symbol_version('__gnu_Unwind_Find_exidx'),
    ('vendor/lib/libnvram.so', 'vendor/lib64/libnvram.so'): blob_fixup()
        .add_needed('libbase_shim.so'),
    'vendor/lib/libui-v30.so': blob_fixup()
        .replace_needed('android.hardware.graphics.common-V1-ndk_platform.so', 'android.hardware.graphics.common-V7-ndk.so'),
    'vendor/lib/libwvhidl.so': blob_fixup()
        .add_needed('libcrypto_shim.so'),
    'vendor/lib64/hw/hwcomposer.mt8188.so': blob_fixup()
        .sig_replace('00 20 80 52 bc 6d 00 94 f9 03 00 aa', '00 a6 81 52'),
    ('vendor/lib64/lib3a.ae.pipe.so', 'vendor/lib64/lib3a.awbsync.so', 'vendor/lib64/lib3a.flash.so',
     'vendor/lib64/lib3a.sensors.color.so', 'vendor/lib64/lib3a.sensors.flicker.so',
     'vendor/lib64/libSQLiteModule_VER_ALL.so', 'vendor/lib64/libaaa_toneutil.so'): blob_fixup()
        .add_needed('liblog.so'),
    'vendor/lib64/lib3a.af.assist.utils.so': blob_fixup()
        .sig_replace('10 00 00 b0 11 aa 41 f9 10 42 0d 91 20 02 1f d6', 'e0 03 1f 2a c0 03 5f d6'),
    ('vendor/lib64/libaalservice.so', 'vendor/lib64/libcam.utils.sensorprovider.so'): blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),
    'vendor/lib64/libcamalgo.platform2.so': blob_fixup()
        .sig_replace('10 00 00 b0 11 2e 41 f9 10 62 09 91 20 02 1f d6', 'e0 03 1f 2a c0 03 5f d6'),
    'vendor/lib64/libmtkcam_hal_android_app_cbadaptor.so': blob_fixup()
        .replace_needed('android.frameworks.displayservice@1.0.so',
                        'lineage.frameworks.displayservice@1.0.so')
        .binary_regex_replace(
            b'_ZN7android10frameworks14displayservice',
            b'_ZN7lineage10frameworks14displayservice')
        .binary_regex_replace(
            _displayservice_unresolved,
            lambda m: _displayservice_ping.ljust(len(m.group(0)), b'\x00')),
    'vendor/lib64/libmtkcam_imgbuf_v2.so': blob_fixup()
        .sig_replace('30 00 00 d0 11 56 43 f9 10 a2 1a 91 20 02 1f d6', 'e0 03 1f 2a c0 03 5f d6'),
}  # fmt: skip

module = ExtractUtilsModule(
    'sunstone',
    'amazon',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
