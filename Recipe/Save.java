
import java.util.Date;

public class Save {
    private final String num;
    private final Date date;

    public Save(String num) {
        this.num = num;
        this.date = new Date();
    }

    public String getNum() {
        return num;
    }

    public Date getDate() {
        return date;
    }
}