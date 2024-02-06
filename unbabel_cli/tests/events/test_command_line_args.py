from click.testing import CliRunner
from unbabel_cli.main import main

def test_main():
    runner = CliRunner()

    # Test with default arguments
    result = runner.invoke(main)
    assert result.exit_code == 0

    # Test with custom arguments
    result = runner.invoke(main, ['--input_file', 'events.json', '--window_size', '15'])
    assert result.exit_code == 0

    # Test with invalid window size
    result = runner.invoke(main, ['--window_size', '5'])
    assert result.exit_code != 0

    # Test with invalid file type
    result = runner.invoke(main, ['--input_file', 'events.txt'])
    assert result.exit_code != 0

    # Test with invalid file type format
    result = runner.invoke(main, ['--input_file', 123])
    assert result.exit_code != 0

    # Test with invalid window size type format
    result = runner.invoke(main, ['--input_file', 'events.json', '--window_size', 'asd'])
    assert result.exit_code != 0
    
    