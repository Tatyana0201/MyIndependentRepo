
Feature:  Login Page Tests
@smoke
  Scenario: Login with valid credentials
    Given Open "dev"environment
     Then T.A. Input following credentials
      | username | password |
      | test | FjeKB9ySMzwvDUs2XACpfu |



