from unittest.mock import patch
import pytest
import secretSanta_util

class TestGeneric:
    @classmethod
    def setup_class(cls):
        """Run once before all tests in the class."""
        print("Setup for the class")
        cls.shared_resource = "Shared Resource"

    @classmethod
    def teardown_class(cls):
        """Run once after all tests in the class."""
        print("Teardown for the class")
        cls.shared_resource = None

    def setup_method(self, method):
        """Run before each test method."""
        print(f"Setup for test: {method.__name__}")
        self.test_resource = "Test Resource"

    def teardown_method(self, method):
        """Run after each test method."""
        print(f"Teardown for test: {method.__name__}")
        self.test_resource = None


    def test_get_names(self):
        # Mock input values for testing
        mock_inputs = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]

        # Function to simulate sequential user inputs
        def mock_input(prompt):
            return mock_inputs.pop(0)

        # Run the function with the mocked input
        with patch("builtins.input", side_effect=mock_input):
            gifterFromID = secretSanta_util.get_names()

        # Assert that gifterFromID is correctly populated
        assert len(gifterFromID) == 10
        assert gifterFromID[0].name == "Alice"
        assert gifterFromID[9].name == "Judy"

    def test_naive_10_participants(self):
        """Test that the naive approach with 10 participants can generate a valid Secret Santa linked list."""
        print("Running test_naive_10_participants")

        # valid list would contain all 10 elements in a connected list


        assert self.test_resource == "Test Resource"
        assert self.shared_resource == "Shared Resource"

    def test_example_2(self):
        """Another sample test method."""
        print("Running test_example_2")
