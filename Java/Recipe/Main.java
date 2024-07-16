

public class Main {
    public static void main(String[] args) {
        Recipe recipe = new Recipe();
        MemRecipe recipe2 = new MemRecipe();

        System.out.println("Creating new recipe");
        recipe.setRecipe("bread, tomato, tost");
        System.out.println(recipe);
        System.out.println("Saving recipe");
        recipe2.setSave(recipe.save());
        System.out.println("Next recipe...");
        
        
    }
}