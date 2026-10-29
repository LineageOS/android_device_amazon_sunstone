#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base.mk)

# Inherit from device makefile.
$(call inherit-product, device/amazon/sunstone/device.mk)

# Inherit some common LineageOS stuff.
$(call inherit-product, vendor/lineage/config/common_full_tablet_wifionly.mk)

PRODUCT_NAME := lineage_sunstone
PRODUCT_DEVICE := sunstone
PRODUCT_MANUFACTURER := Amazon
PRODUCT_BRAND := Amazon
PRODUCT_MODEL := KFSNWI
PRODUCT_CHARACTERISTICS := tablet

PRODUCT_GMS_CLIENTID_BASE := android-amazon

PRODUCT_SYSTEM_PROPERTIES += \
    ro.product.manufacturer=AMAZO

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="turquoise-user 16 SL16SHIP2003 1344N amz-p,release-keys" \
    BuildFingerprint=Amazon/turquoise/turquoise:16/SL16SHIP2003/1344N:user/amz-p,release-keys \
    DeviceProduct=sunstone
