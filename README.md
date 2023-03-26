# Gauntlet

### Requirements

- Python 3.6+

### Installation

1. Clone the repository
```
git clone https://github.com/woop/gauntlet.git
```

2. Navigate to the `gauntlet` directory
```
cd gauntlet
```

### Usage

Run `main.py` from the command line:

```
python main.py <action> <key> <input_file> <output_file>
```

- `action`: Use `secure` or `verify`
- `key`: Your secret key
- `input_file`: Path to the input file
- `output_file`: Path to the output file

#### Example

Secure data:

```
python main.py secure mysecretkey input.txt secured_output.txt
```

Verify data:

```
python main.py verify mysecretkey secured_output.txt verification_results.txt
```

### Tests

To run tests, execute the following command in the `gauntlet` directory:

```
python -m unittest discover tests
```
