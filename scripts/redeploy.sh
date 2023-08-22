#!/bin/bash

rm -rf target/deploy

cargo build-sbf > /dev/null 2>&1

solana program deploy target/deploy/*.so

PROGRAM_ID=$(solana address --keypair target/deploy/*.json)
PDA=$(solana find-program-derived-address BPFLoaderUpgradeab1e11111111111111111111111 pubkey:$PROGRAM_ID)

echo "Redeployed program at: $PROGRAM_ID"
solana account $PDA | grep "Length:" 