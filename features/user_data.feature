Feature: Market data tests

  Scenario: Retrieve Open Orders
     Given API is accessible
      When we retrieve open orders
      Then "0" open orders exists!

      