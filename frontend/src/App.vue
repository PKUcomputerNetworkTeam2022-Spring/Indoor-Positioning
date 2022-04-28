<style scoped>
 .navbar.navbar-dark.bg-dark{
    background-color: #AABB55!important;
 }
</style>

<template>
  <div id="app">
    <!-- NavBar -->
    <div>
      <b-navbar toggleable="lg" type="dark" variant="dark">
        <div class="container">
          <b-navbar-brand href="#">Indoor Positioning</b-navbar-brand>
        </div>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item href="#">Admin</b-nav-item>
            
            <!-- Positioning Button -->
            <b-nav-item href="#" v-b-modal.modal-1>Positioning
              <b-modal id="modal-1" title="Get Position">
                <template #modal-header="{ close }">
                  <h5>MAC of the target device</h5>
                </template>
                <b-form inline>
                  <b-form-input
                    id="inline-form-input-name"
                    class="mb-2 mr-sm-2 mb-sm-0"
                    placeholder="Please enter the correct MAC."
                  ></b-form-input>
                  <b-button variant="primary" @click="onPosition">Save</b-button>
                </b-form>

              </b-modal>
            </b-nav-item>
          
          </b-navbar-nav>

        </b-collapse>
      </b-navbar>
    </div>

    <b-container class="bv-example-row">
      <b-row>
        <b-col>
          <!-- Scatter Plot for Track Display -->
          <div class="shadow p-3 mb-5 bg-white rounded">
            <b-card
              title="Track Display"
              style="max-width: 80rem;"
              class="mb-2"
            >
              <div>
                <Scatterplot 
                  id="comp1" 
                  :data='[]'
                  :selection="[]" 
                  :encoding="{ x: 'West-East', y: 'North-South' }"
                  @brush="onBrush" 
                />
              </div>
            </b-card>
          </div>
        </b-col>
        <b-col>
          <!-- Draw Circle to Show Positioning -->
          <div class="shadow p-3 mb-5 bg-white rounded">
            <b-card
              title="Positioning Detail"
              style="max-width: 80rem;"
              class="mb-2"
            >
              <div>
                <v-stage :config="configKonva">
                  <v-layer>
                    <v-circle :config="f4041c"></v-circle>
                    <v-circle :config="f40443"></v-circle>
                    <v-circle :config="f40444"></v-circle>
                    <v-circle :config="f4041c_center"></v-circle>
                    <v-circle :config="f40443_center"></v-circle>
                    <v-circle :config="f40444_center"></v-circle>
                    <v-star :config="real_pos"></v-star>
                    <v-regular-polygon :config="pos"></v-regular-polygon>
                    <v-text :config="real_pos_coordinate"></v-text>
                    <v-text :config="pos_coordinate"></v-text>
                  </v-layer>
                </v-stage>
              </div>
            </b-card>
          </div>
        </b-col>
      </b-row>
    </b-container>
    
  </div>
</template>

<script>
import Scatterplot from './components/Scatterplot'
import _ from 'lodash'

export default {
  props: {

    points: {
      type: Array,
      required: true,
    },

  },
  data () {
    return {
      form: {

      },
      selection: [],
      trace_points: [],
      configKonva: {
        width: 500,
        height: 520,
        opacity: 0.8
      },
      f4041c: {
        x: 30*0+100,
        y: 450-30*0,
        radius: 1,
        fill: "green",
        stroke: "black",
        strokeWidth: 2
      },
      f4041c_center: {
        x: 30*0+100,
        y: 450-30*0,
        radius: 2,
        fill: "black",
        stroke: "black",
        strokeWidth: 2
      },
      f40443: {
        x: 30*0+100,
        y: 450-30*10.2,
        radius: 1,
        fill: "yellow",
        stroke: "black",
        strokeWidth: 2
      },
      f40443_center: {
        x: 30*0+100,
        y: 450-30*10.2,
        radius: 2,
        fill: "black",
        stroke: "black",
        strokeWidth: 2
      },
      f40444: {
        x: 30*6.4+100,
        y: 450-30*10.2,
        radius: 1,
        fill: "orange",
        stroke: "black",
        strokeWidth: 2
      },
      f40444_center: {
        x: 30*6.4+100,
        y: 450-30*10.2,
        radius: 2,
        fill: "black",
        stroke: "black",
        strokeWidth: 2
      },
      real_pos: {
        x: -100,
        y: -100,
        numPoints: 6,
        innerRadius: 3,
        outerRadius: 5,
        fill: 'red',
        stroke: 'black',
        strokeWidth: 1,
      },
      pos: {
        x: -100,
        y: -100,
        sides: 6,
        radius: 5,
        fill: 'blue',
        stroke: 'black',
        strokeWidth: 1,
      },
      real_pos_coordinate: {
        x: -100,
        y: -100,
        text: "Real Pos: (1.25, 1.25)",
        fontsize: 18,
        fontFamily: "Calibri",
        fill: "black",
      },
      pos_coordinate: {
        x: -100,
        y: -100,
        text: "Estimated Pos: (1.00, 1.50)",
        fontsize: 18,
        fontFamily: "Calibri",
        fill: "black",
      }
    }
  },
  methods: {
    onBrush(selectedPts) {
      const newPts = _.differenceBy(selectedPts, this.selection, 'id')
      if (newPts.length > 0) {
        this.selection = selectedPts
      }
    },
    onPosition() {
      this.real_pos["x"] = 50;
      this.real_pos["y"] = 50;
      this.pos["x"] = 60;
      this.pos["y"] = 60;
      this.f4041c["radius"] = 50;
      this.f40443["radius"] = 70;
      this.f40444["radius"] = 80;
      const path = "http://localhost:8000";
      axios.post(path, JSON.stringify(loginInfo)).then(function (response) {
        console.log("i accept");
        var login_result = response.data;
        is_login_success = login_result["result"];
        if (is_login_success == "success") {
          //alert("登陆成功");
          var mymes=confirm("登陆成功");
          if(mymes==true){
            that.$router.push({ path: "/", query: { from: "login" } });
          }
          GLOBAL.currentUser_ID = login_result["id"];
          GLOBAL.currentUser_name = login_result["user_name"];
          GLOBAL.isLogined = true;
          GLOBAL.view = "myCenter";
          GLOBAL.isLogined = true;
        } else if (is_login_success === "failed") {
          alert("登陆失败");
          this.name = "";
          this.password = "";
        } else {
          alert("传参失败");
        }
      });
    }
  },
  components: {
    Scatterplot
  }
}
</script>

<style>
#app {

}
</style>