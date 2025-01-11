void main() {
  /// for loop
  //

  // for (int i = 0; i <= 1000; i++) {
  //   print("$i");
  // }

  /// for in loop
  List data = [1, 2, 3, 4, 5, 6];
  List names = ['Daniel', "Ajayi", "Akin", 9, 5.5];

  // for (int i in data) {
  //   print(i + 2);
  // }

  /// for each loop
  // names.forEach((var i) {
  //   print(i);
  // });

  /// while loop
  // int i = 1;
  // while (i <= 10) {
  //   print(i);
  //   i++;
  // }

  /// do-while loop
  // do {
  //   print(i + 1);
  //   i++;
  // } while (i < 5);

  /// Task 1: write a dart code that checks if the number "4" is inside the
  /// given list.

  List givenList = [2, 6, 7, 8, 10, 4, 20];

  // for (int i in givenList) {
  //   if (i == 4) {
  //     print("I found 4");
  //   }
  // }

  /// Task 2: write a dart code that checks if the number "20" is inside the
  /// given list.

  // for (int i in givenList) {
  //   if (i == 20) {
  //     print("I found 4");
  //   }
  // }

  /// Question: Write a Dart program to print numbers from 1 to 10 using a for loop.
  // for (int i = 1; i <= 10; i++) {
  //   print(i);
  // }

  /// Question: Write a Dart program to calculate the sum of numbers from 1 to 100 using a for loop.

  //create a variable and give it a value of 0
  //steps: print 1 -100
  // int sum = 0;
  // for (int i = 1; i <= 100; i++) {
  //   sum += i;
  // }
  // print(sum);

  /// Question: Write a Dart program to print all even numbers between 1 and 20 using a loop
  // for (int o = 1; o <= 20; o++) {
  //   if (o % 2 == 0) {
  //     print(o);
  //   }
  // }

  /// Question: Write a Dart program to print all odd numbers between 1 and 20 using a loop
  // for (int o = 1; o <= 20; o++) {
  //   if (o % 2 == 1) {
  //     print(o);
  //   }
  // }

  // Question: Write a Dart program to reverse a list using a loop.
  // List mainList = [1, 2, 3, 4, 5, 6];

  // List reversedList = [];

  // for (int i = mainList.length - 1; i >= 0; i--) {
  //   reversedList.add(mainList[i]);
  // }
  // print(reversedList);

  //Question: Write a Dart program to find the maximum number in a list using a loop.
  // List numbers = [
  //   2,
  //   3,
  //   4,
  //   1,
  //   0,
  // ];
  // int max = 0;

  // for (int num in numbers) {
  //   if (num > max) {
  //     max = num;
  //   }
  // }
  // print(max);

  /// Question: Write a Dart program to print the multiplication table of a number.
  int number = 70;

  for (int i = 1; i <= 5; i++) {
    // 5 * 1 = 5
    print('$number x $i = ${number * i}');
  }

  /// Question: Write a Dart program to count the number of vowels in a string using a loop.
  String input = "hello world";
  int count = 0;
  String vowels = "aeiou";

  for (int i = 0; i < input.length; i++) {
    if (vowels.contains(input[i])) {
      count++;
    }
  }

  print('Number of vowels: $count');
}
