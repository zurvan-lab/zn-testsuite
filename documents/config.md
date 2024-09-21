# config

to run a test on your relay you have to provide a config file. this document provides the exact detail
about each section in config.

each config is a `.json` file with following details:

* `"name"`, is a human-readable name for config.

eample values:

- `"my nostr rust relay normal test."`
- `"immortal load test."`

* `"target"`, is the address of relay you wan't to be tested.

example values:

- `"ws://localhost:7777"`
- `"ws://127.0.0.1:7777"`
- `"wss://relay.example.com"`
- `"wss://relay.example.com:7777"`

* `"tests"`, is object which contains some keys, which are testing model names, pointing to objects
that are defining config for that specific case. below is the list of all supported models and their config document.

#### protocol

the protocol model tests if the given address runs a nostr relay which implemented the protocol (NIPS) correctly.
there is no specific load, fuzz or stress in this model.

and example test object for this model:

```jsonc
{
  "name": "immortal relay basic test.", // defined in other sections.
  "target": "ws://localhost:7777",     // defined in other sections.
  "tests": { // defined in other sections.
    "protocol": { // test model.
      "outdir": "/reports/znrt_immo", // the directory that going to contain the result of test.
      "cases": ["*"],                 // test cases to be executed.
      "excluded_cases": []            // if you want to exclude any case.
      // provide 2 keys that are able to read and write to relay.
      "whitelisted_key1": "e86703b8f6cf3631b1110c0a26676e1c43023c65fb9879d9129c942c06b2e8db",
      "whitelisted_key2": "e86703b8f6cf3631b1110c0a26676e1c43023c65fb9879d9129c942c06b2e8db"
    }
  }
}
```

here is the lits of test cases for `protocol` model:

- `NIP-<X>`, tests an specific NIP and makes sure that it is implemented correctly.
- `ZNRP`, znr protocol model test cases. (todo(?)),
