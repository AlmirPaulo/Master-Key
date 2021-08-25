new Vue({
    el:"#app",
    delimiters:['[[',']]'],
    template: `
        <main>
            <div class="container">
            <table class="table table-striped table-secondary">
              <thead>
                <tr>
                  <th scope="col">Service</th>
                  <th scope="col">Show Password</th>
                  <th scope="col">Edit</th>
                  <th scope="col">Delete</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                <!--td>services here</td-->
                </tr>
                <tr>
                <!--td>show passwords btns here</td-->
                </tr>
                <tr>
                <!--td>Edit buttons here</td-->
                </tr>
                <tr>
                    <!--td>delete btns here</td-->
                </tr>
          </tbody>
        </table>
            </div>
        </main>
    `,


})
