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
     var elapsed = Math.round(this.props.elapsed  / 100);
     var seconds = elapsed / 10 + (elapsed % 10 ? '' : '.0' );
     var message =
       'React has been successfully running for ' + seconds + ' seconds.';

     return React.DOM.p(null, message);
   }
 });

 // Call React.createFactory instead of directly call ExampleApplication({...}) in React.render
 var ExampleApplicationFactory = React.createFactory(ExampleApplication);

 var start = new Date().getTime();
 setInterval(function() {
   ReactDOM.render(
     ExampleApplicationFactory({elapsed: new Date().getTime() - start}),
     document.getElementById('container')
   );
 }, 50);
