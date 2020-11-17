
import java.util.Date;


public class Recipe {
    private String recipe;
    private Date date;

    public void setRecipe(String recipe) {
        this.recipe = recipe;
        this.date = new Date();
    }

    public Save save() {
        return new Save(recipe);
    }

    public void load(Save save) {
        date = save.getDate();
        recipe  = save.getrecipe();
    }
    
    @Override
    public String toString() {
        return "Recipe: " + recipe + "\nDate: " + date + "\n";
    }
}