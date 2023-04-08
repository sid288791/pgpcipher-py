# This is a sample Python script.
from openPGP.DecryptionByPrivKey import decByPrivKey
from openPGP.EncryptionByPubKey import encByPubKey


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    pgp_pub_key = ''
    file_to_enc = ''
    enc_output_file = ''
    encByPubKey(pgp_pub_key, file_to_enc, enc_output_file)

    pgp_priv_key = ''
    phassphrase = ''
    enc_file = ''
    dec_output_file = ''
    decByPrivKey(pgp_priv_key, phassphrase, enc_file, dec_output_file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
