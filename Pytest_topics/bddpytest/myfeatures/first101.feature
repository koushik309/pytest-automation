Feature: Bank Transactions
    Tests pertaining to banking transations like withdrawal, deposit

  Scenario: Withdrawal of money
    Given the account balance is 100
    When the account holder withdraws 30
    Then the account balance should be 70

