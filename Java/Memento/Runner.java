

public class Runner {
    public static void main(String[] args) {
        Step step = new Step();
        MementoXO game = new MementoXO();

        System.out.println("Creating new game");
        step.setStep("A12");
        System.out.println(step);
        System.out.println("Saving step");
        game.setSave(step.save());
        System.out.println("Next step...");
        System.out.println("No back!");
        step.load(game.getSave());
        
    }
}