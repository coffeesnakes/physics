const express = require('express');
const app = express();

// Middleware for parsing JSON and urlencoded form data
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.use('/api/users', require('./routes/users'));
app.use('/api/courses', require('./routes/courses'));
app.use('/api/lessons', require('./routes/lessons'));

// Start server
const port = process.env.PORT || 1337;
app.listen(port, () => console.log(`Server running on port ${port}`));