import mypack.Calculator;

class TestPackage {
    public static void main(String[] args) {
        Calculator obj = new Calculator();
        System.out.println("Addition: " + obj.add(10, 5));
        System.out.println("Subtraction: " + obj.sub(10, 5));
    }
}