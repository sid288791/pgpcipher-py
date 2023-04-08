import gnupg


def encryptByPubKey(pgp_pub_key, file_to_enc, output_file):
    gpg = gnupg.GPG()

    with open(pgp_pub_key) as f:
        key_data = f.read()
    print(key_data)

    with open(pgp_pub_key) as f:
        key_data = f.read()
    import_result = gpg.import_keys(key_data)

    for k in import_result.results:
        print(k)

    pub_keys = gpg.list_keys()

    fingeprint = import_result.fingerprints[0]
    print(fingeprint)

    gpg.trust_keys(fingeprint, 'TRUST_ULTIMATE')

    with open(file_to_enc, 'rb') as f:
        status = gpg.encrypt_file(f, recipients=fingeprint, output=output_file, passphrase='pass', armor=True)

    print(status.ok)
    print(status.status)
    print(status.stderr)
    print('~' * 50)
