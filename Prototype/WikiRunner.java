

public class WikiRunner {
    public static void main(String[] args) {
        WikiPrototype prototype = new WikiPrototype(1, "Java", "Java - programming language");
        System.out.println(prototype);

        WikiFactory factory = new WikiFactory(prototype);
        WikiPrototype prototype2 = factory.clonePrototype();
        System.out.println(prototype2);
    }
}