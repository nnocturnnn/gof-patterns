

public class WikiPrototype implements Copyable {
    private int id;
    private String projectName;
    private String sourceCode;

    public WikiPrototype(int id, String projectName, String sourceCode) {
        this.id = id;
        this.projectName = projectName;
        this.sourceCode = sourceCode;
    }

    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public void setProjectName(String projectName) {
        this.projectName = projectName;
    }
    public String getProjectName() {
        return projectName;
    }
    public String getSourceCode() {
        return sourceCode;
    }
    public void setSourceCode(String so) {
        this.sourceCode = so;
    }
    @Override
    public Object copy() {
        WikiPrototype copy = new WikiPrototype(id, projectName, sourceCode);
        return copy;
    }
    @Override
    public String toString() {
        return "Wiki{" + 
                "id=" + id +
                ",projectName=" + projectName +
                ",sourceCode=" + sourceCode + "}";
    }
}