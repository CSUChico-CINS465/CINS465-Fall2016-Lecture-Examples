// var Hello = React.createClass({
//   render: function(){
//     return <div> Hello {this.props.name}</div>;
//   }
// });
//
// ReactDOM.render(
//   <Hello name="World"/>,
//   document.getElementById('container')
// )

// var Hello = React.createClass({
//   render: function(){
//     return <div> Hello {this.props.name}</div>;
//   }
// });
//
// ReactDOM.render(
//   <Hello name="World"/>,
//   document.getElementById('container')
// )
var ExampleApplication = React.createClass({
   render: function() {
     var message = this.props.data.suggestions
     return React.DOM.p(null, JSON.stringify(this.props.data.suggestions));
   }
 });

 // Call React.createFactory instead of directly call ExampleApplication({...}) in React.render
 var ExampleApplicationFactory = React.createFactory(ExampleApplication);

 var start = new Date().getTime();
 var update = setInterval(function() {
  $.ajax({
    url: "/suggestions",
    success: function(data) {
      //console.log(data);
      ReactDOM.render(
          ExampleApplicationFactory({data: data}),
          document.getElementById('container'));
    }
  })
}, 500);
