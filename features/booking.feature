Feature: Goibibo
  Background:
    Given launch chrome broweser
    When open the goibibo browser
  Scenario Outline: choose places
    Then enter the arrival place "<arival>"
    And  enter the destination place "<destination>"
    And click on search
     And apply filter1
    And  apply filter2
    And click on SELECT SEAT button
    And  select boarding point
    And  select dropping point
    And  select your seat
    And  click on CONTINUE
    And apply Insurence
    And enter the passenger name
    And  enter the passenger age
    And select gender
    And enter the passenger email
    And enter the passenger mobile
    And click on pay
    Examples:
        |arival       |destination |
        | latur       | mumbai     |
        | latur       | pune       |
        |solapur    | pune       |
        | pune        | bengalore  |
        | nashik      | mumbai     |
        | swarget     | mumbai     |






























