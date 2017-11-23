#!/bin/sh
#
# Testing code for Micropython.
#
# Uses the micropython (unix) binary to run Unittest code. No py.test
# or tox available yet for micropython.
#
set -ex

MPY=micropython

#$MPY tests/bc_transaction_test.py

$MPY tests/test_serialize.py
$MPY tests/encoding_test.py
$MPY tests/pure_ripemd_test.py
$MPY tests/ecdsa/generator_test.py
$MPY tests/ecdsa/libsecp256k1_test.py
$MPY tests/chainfinder_test.py

# slow... but correct (keep last)
#$MPY tests/ecdsa/ecdsa_test.py

$MPY tests/bip32_test.py
$MPY tests/blockchain_test.py
$MPY tests/build_tx_test.py
$MPY tests/cmds/block_test.py
$MPY tests/cmds/cmdline_test.py
$MPY tests/cmds/ToolTest.py
$MPY tests/cmds/tx_test.py
$MPY tests/electrum_test.py
$MPY tests/key_test.py
$MPY tests/key_translation_test.py
$MPY tests/key_validate_test.py
$MPY tests/message_test.py
$MPY tests/msg_signing_test.py
$MPY tests/multisig_individual_test.py
$MPY tests/parse_block_test.py
$MPY tests/pay_to_test.py
$MPY tests/segwit_test.py
$MPY tests/services/services_test.py
$MPY tests/sighash_single_test.py
$MPY tests/signature_test.py
$MPY tests/tools_test.py
$MPY tests/tx_test.py
$MPY tests/tx_utils_test.py
$MPY tests/validate_tx_test.py
$MPY tests/vm_script_test.py
$MPY tests/who_signed_test.py
