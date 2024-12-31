from unittest.mock import patch
import pytest
import time
import secretSanta_util
import secretSanta_naiveRandomize
import secretSanta_smartRandomize

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

        # Mock input values for testing
        mock_inputs = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
        # Function to simulate sequential user inputs
        def mock_input(prompt):
            return mock_inputs.pop(0)

        # Run the function with the mocked input
        with patch("builtins.input", side_effect=mock_input):    
            gifterFromID = secretSanta_util.get_names()

        # trigger the naive randomization assignment
        start_time = time.time()  # Record the start time
        head = secretSanta_naiveRandomize.createSecretSantaAssignments(gifterFromID)
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate elapsed time
        print(f"Elapsed time: {elapsed_time}")

        # Traverse the linked list and ensure we have a valid Secret Santa assignment
        cur = head
        counter = 0
        while cur.gifted_to is not None and counter < 10:
            print(f"{cur.name} --> ")
            cur = cur.gifted_to
            counter += 1

        # Assert that the linked list is correctly formed
        assert counter == 10

    def test_smart_10_participants(self):
        """Test that the smart randomize approach with 10 participants can generate a valid Secret Santa linked list."""
        print("Running test_naive_10_participants")

        # Mock input values for testing
        mock_inputs = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
        # Function to simulate sequential user inputs
        def mock_input(prompt):
            return mock_inputs.pop(0)

        # Run the function with the mocked input
        with patch("builtins.input", side_effect=mock_input):    
            gifterFromID = secretSanta_util.get_names()

        # trigger the naive randomization assignment        
        start_time = time.time()  # Record the start time
        head = secretSanta_smartRandomize.createSecretSantaAssignments(gifterFromID)
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate elapsed time
        print(f"Elapsed time: {elapsed_time}")

        # Traverse the linked list and ensure we have a valid Secret Santa assignment
        cur = head
        counter = 0
        while cur.gifted_to is not None and counter < 10:
            print(f"{cur.name} --> ")
            cur = cur.gifted_to
            counter += 1

        # Assert that the linked list is correctly formed
        assert counter == 10

    # def test_naive_100_participants(self):