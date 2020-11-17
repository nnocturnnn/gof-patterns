
import java.util.Date;

public class Save {
    private final String recipe;
    private final Date date;

    public Save(String recipe) {
        this.recipe = recipe;
        this.date = new Date();
    }

    public String getNum() {
        return recipe;
    }

    public Date getDate() {
        return date;
    }
}