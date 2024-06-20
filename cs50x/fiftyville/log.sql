-- Keep a log of any SQL queries you execute as you solve the mystery.

-- find the crime report for the theft
select description
from crime_scene_reports
where year = 2021
and month = 7
and day = 28
and street = "Humphrey Street";

-- get the witnesses information
select name, transcript
from interviews
where year = 2021
and month = 7
and day = 28;

-- get the detailes of every owner of the license plates of interest from the security cam footage one of the witnesses (Ruth) mentioned
select name
from people
where license_plate in (
    select license_plate
    from bakery_security_logs
    where year = 2021
    and month = 7
    and day = 28
    and hour = 10
    and minute >= 15
    and minute <= 25
)

intersect

-- get atm transaction details of atm withdrawal witness Eugene mentioned
select people.name
from ((atm_transactions
inner join bank_accounts
on bank_accounts.account_number = atm_transactions.account_number)
inner join people
on people.id = bank_accounts.person_id)
where year = 2021
and month = 7
and day = 28
and atm_location = "Leggett Street"
and transaction_type = "withdraw"

intersect

-- the witness Raymond mentions the thief making a call, get the name of the callers at the time of the robbery
select people.name
from phone_calls
inner join people
on people.phone_number = phone_calls.caller
where year = 2021
and month = 7
and day = 28
and duration <= 60

intersect

-- Raymond's statement mentions the caller wanting a ticket for an early flight the next day
-- get the name of people on the first flight out of Fiftyville the day after robbery
select people.name
from ((people
inner join passengers
on passengers.passport_number = people.passport_number)
inner join flights
on passengers.flight_id = flights.id)
where flights.hour = 8
and year = 2021
and month = 7
and day = 29
and flights.origin_airport_id = (
    select id
    from airports
    where city = "Fiftyville"
);

-- from the result of the previous queries Bruce seems to be the common denominator for all the clues provides therefore he's the thief

-- get the name of the city thief (Bruce) flew to day after the robbery
select airports.city
from (((airports
inner join flights
on flights.destination_airport_id = airports.id)
inner join passengers
on passengers.flight_id = flights.id)
inner join people
on people.passport_number = passengers.passport_number)
where people.name = "Bruce"
and year = 2021
and month = 7
and day = 29;

-- get theif's number to use for finding his accomplise
select phone_number
from people
where name = "Bruce";

-- get the name of accomplice thief called at time of robbery
select people.name
from people
inner join phone_calls
on people.phone_number = phone_calls.receiver
where phone_calls.caller = "(367) 555-5533"
and year = 2021
and month = 7
and day = 28
and duration <= 60;

