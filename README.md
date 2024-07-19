# GOF Patterns
My vision and realization GOF Patterns 
### Creational Patterns
1. **Singleton** - allows you to create only one instance of an object.  
   *Example: only one Database connection.*
2. **Factory Method** - allows creating different instances of objects using a dictionary, avoiding IF statements.  
   *Example: GET, POST, PUT, DELETE handlers.*
3. **Abstract Factory** - allows creating a factory of factories.  
   *Example: Factory of Factories.*
4. **Prototype** - creates new objects by copying an existing object (deep copy).  
   *Example: base Docker container.*
5. **Builder** - allows creating complex objects part by part.  
   *Example: building an SQL query (Base, Filters, Limits, Sorts).*

### Structural Patterns
1. **Adapter** - allows incompatible interfaces to work together.  
   *Example: connecting Internal and External APIs.*
2. **Bridge** - helps connect one interface to another.  
   *Example: connecting SQL and NoSQL databases through a bridge.*
3. **Facade** - provides a simplified interface to a complex system.  
   *Example: Interface to all Microservices.*
4. **Composite** - helps to work with objects and nested objects of the same type.  
   *Example: Module manager with a hierarchical structure.*
5. **Decorator** - extends the functionality of an object.  
   *Example: Python decorator.*
6. **Flyweight** - helps use less memory and time by sharing as much data as possible.  
   *Example: caching strategy in backend systems.*
7. **Proxy** - adds a level of abstraction before accessing an object.  
   *Example: like VPN or Authorization.*

### Behavioural Patterns
1. **Memento** - captures and restores an object's internal state.  
   *Example: GIT snapshot of a repository.*
