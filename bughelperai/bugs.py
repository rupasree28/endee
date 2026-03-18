bugs_data = [

# Java Errors
{
"error": "NullPointerException in Java",
"cause": "Object not initialized or referencing null object",
"fix": "Initialize object before use and add null checks"
},
{
"error": "IndexOutOfBoundsException",
"cause": "Accessing index outside array/list range",
"fix": "Validate index before accessing"
},
{
"error": "ClassNotFoundException",
"cause": "Class not available in classpath",
"fix": "Check dependencies and classpath configuration"
},
{
"error": "NumberFormatException",
"cause": "Invalid string to number conversion",
"fix": "Validate input before parsing"
},

# Python Errors
{
"error": "TypeError in Python",
"cause": "Wrong datatype used in operation",
"fix": "Check variable types before operation"
},
{
"error": "IndentationError",
"cause": "Improper indentation",
"fix": "Fix spacing and indentation alignment"
},
{
"error": "KeyError",
"cause": "Dictionary key not found",
"fix": "Check key exists before accessing"
},
{
"error": "ModuleNotFoundError",
"cause": "Module not installed",
"fix": "Install module using pip"
},

# Web/API Errors
{
"error": "404 Not Found",
"cause": "Wrong API endpoint or URL",
"fix": "Verify endpoint path"
},
{
"error": "500 Internal Server Error",
"cause": "Backend server crash or bug",
"fix": "Check server logs"
},
{
"error": "403 Forbidden",
"cause": "Unauthorized access",
"fix": "Check authentication permissions"
},

# SQL Errors
{
"error": "SQLSyntaxErrorException",
"cause": "Incorrect SQL syntax",
"fix": "Check query syntax carefully"
},
{
"error": "Duplicate Entry SQL Error",
"cause": "Unique constraint violation",
"fix": "Check existing records before insert"
},

# Frontend Errors
{
"error": "Cannot read property of undefined",
"cause": "Accessing undefined object",
"fix": "Check object exists before access"
},
{
"error": "Unexpected token < in JSON",
"cause": "Invalid API response format",
"fix": "Check API response"
}
]