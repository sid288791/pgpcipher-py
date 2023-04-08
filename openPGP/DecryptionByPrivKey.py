import gnupg


def decryptByPrivKey(priv_key_file, passphrase, enc_file, output_file):
    gpg = gnupg.GPG()

    key_data = open(priv_key_file, 'rb').read()

    import_result = gpg.import_keys(key_data)
    print(import_result.results)

    gpg.list_keys(secret=True)
    gpg.list_keys()

    with open(enc_file, 'rb') as f:
        status = gpg.decrypt_file(f, passphrase=passphrase, output=output_file)

    print(status.ok)
    print(status.status)
    print(status.stderr)
    print('~' * 50)
