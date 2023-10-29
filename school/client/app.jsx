import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './components/HomePage';
import CoursePage from './components/CoursePage';
import LessonPage from './components/LessonPage';
import UserProfile from './components/UserProfile';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={HomePage} />
        <Route path="/courses/:id" component={CoursePage} />
        <Route path="/lessons/:id" component={LessonPage} />
        <Route path="/profile" component={UserProfile} />
      </Switch>
    </Router>
  );
}

export default App;da