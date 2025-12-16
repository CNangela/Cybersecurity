import base64

def main():
    val = "Vmxkd1NrNVhVbk5qUlZKU1ltdGFjRlJYZEhOaWJFNVhWR3RPV0dKVmJEWldiR1JyV1ZkS1ZXRXphRnBpVkVaVFYycEtVMU5IUmtobFJYQlRUVmhDTmxZeFdtdGhhelZ5WWtWYWFWSlViRmRVVlZaYVRURmFjbFpyT1ZaV2JXUTJWa1pvYTFkck1YVlVhbHBoVWxack1GUlZaRXRqVmxaMVZHMTRXRkpVUlRCWFdIQkdUbGRHY2s1VmFFOVdNWEJoV1Zkek1XSldaSFJPVm1SclZsZDRXbFJWVm5wUVVUMDk="

    # decodifica in byte
    decoded_bytes = base64.b64decode(val)

    # converti i byte in stringa
    decoded_string = decoded_bytes.decode('utf-8')

    for i in range(5): 
        decoded_bytes = base64.b64decode(decoded_string)
        decoded_string = decoded_bytes.decode('utf-8')
        print(decoded_string)



if __name__ == "__main__":
    main()