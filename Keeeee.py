import winreg

def decode_product_key(digital_product_id):
    # Ez a funkció a digitális termékkulcs dekódolására szolgál
    key = []
    for i in range(52, 67):
        key.append(digital_product_id[i])
    
    # További dekódoló logika szükséges itt
    # Ez egy példa helykitöltő; tényleges dekódolási algoritmus szükséges
    return ''.join(map(chr, key))

def get_license_keys():
    registry_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
    
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path)
        product_name, _ = winreg.QueryValueEx(reg_key, "ProductName")
        digital_product_id, _ = winreg.QueryValueEx(reg_key, "DigitalProductId")
        
        decoded_key = decode_product_key(digital_product_id)
        return {product_name: decoded_key}
        
    except FileNotFoundError:
        return {}

if __name__ == "__main__":
    keys = get_license_keys()
    for product, key in keys.items():
        print(f"{product}: {key}")
