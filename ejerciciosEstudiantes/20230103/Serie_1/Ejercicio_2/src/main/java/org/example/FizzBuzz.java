package org.example;

public class FizzBuzz {

    public String forValue(int value) {
        if (value % 3 == 0 && value % 5 == 0) {
            return "FizzBuzz";
        } else if (value % 3 == 0) {
            return "Fizz";
        } else if (value % 5 == 0) {
            return "Buzz";
        } else {
            return String.valueOf(value);
        }
    }
    
}
