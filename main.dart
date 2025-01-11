void main() {
  /// Question: Write a Dart program to count the number of vowels in a string using a loop.
  const input = 'hello world';
  int count = 0;
  const vowels = 'aeiou';

  for (int i = 0; i < input.length; i++) {
    if (vowels.contains(input[i])) {
      count++;
    }
  }

  print('Number of vowels: $count');
}
