import React from 'react';
import Router from './Router';
import './App.css';
import { BrowserRouter } from 'react-router-dom';
import { LayoutProvider } from 'react-page-layout';
import DefaultLayout from './components/default/DefaultLayout';
import PublicDefaultLayout from './components/default/PublicDefaultLayout';
import PieChart from './components/dashboard/PieChart';

const layouts = {
	'public': PublicDefaultLayout,
	'default': DefaultLayout
};

// const data = {
//   data: [
//     {
//       id: 1,
//       category_name: "Category 1",
//       category_color: "red",
//       total_amount_percent: 20,
//     },
//     {
//       id: 2,
//       category_name: "Category 2",
//       category_color: "#fff",
//       total_amount_percent: 10,
//     },
//     {
//       id: 3,
//       category_name: "Category 3",
//       category_color: "green",
//       total_amount_percent: 70,
//     },
//   ],
// };


function App() {
	return (
    <LayoutProvider layouts={layouts}>
    	<BrowserRouter>
    		<Router />
    	</BrowserRouter>
    </LayoutProvider>

  );
}

export default App;