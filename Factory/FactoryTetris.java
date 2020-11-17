

public class FactoryTetris {
    public static void main(String[] args) {
        Factory factory = new Factory();
        int a = 0;
        int b = 1;
      
        int random_number1 = a + (int) (Math.random() * b);
        int random_number2 = a + (int) (Math.random() * b);
        int random_number3 = a + (int) (Math.random() * b);
        int random_number4 = a + (int) (Math.random() * b);

        Figure fig1 = factory.create(random_number1);
        Figure fig2 = factory.create(random_number2);
        Figure fig3 = factory.create(random_number3);
        Figure fig4 = factory.create(random_number4);
        fig1.beFigure();
        fig2.beFigure();
        fig3.beFigure();
        fig4.beFigure();
    }
}