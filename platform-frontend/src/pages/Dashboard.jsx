import React, { useEffect } from "react";
import "./Dashboard.css";

const Dashboard = () => {
  useEffect(() => {
    const testUserAPI = async () => {
      const token = localStorage.getItem("token");
      console.log("저장된 토큰:", token);

      if (token) {
        try {
          const response = await fetch(
            "https://cmbvknq8pi.execute-api.ap-northeast-2.amazonaws.com/dev/api/user/me",
            {
              headers: {
                Authorization: `Bearer ${token}`,
              },
            }
          );

          console.log("User API 응답:", response.status);
          const userData = await response.json();
          console.log("사용자 데이터:", userData);
        } catch (error) {
          console.error("User API 에러:", error);
        }
      }
    };

    testUserAPI();
  }, []);

  return (
    <section className="dashboard-section">
      <div className="wrap">
        <div className="info-text-container">
          <h3 className="title-text">USER NAME 님의 서비스 이용 현황입니다.</h3>
          <p>
            배포한 프로젝트는 N개 이며, 현재 활성화 프로젝트는 N개, 비활성화
            프로젝트는 N개입니다.
          </p>
        </div>
        <div className="resource-container">
          <div className="memory-container">
            <div className="text-box">
              <p className="title">메모리 사용량</p>
              <p className="usage eng">
                <span className="used">NNN</span>/
                <span className="total">2GB</span>
              </p>
            </div>
            <div className="bar-box">
              <div className="fill-bar"></div>
            </div>
          </div>
          <div className="traffic-container">
            <div className="text-box">
              <p className="title">트래픽 사용량</p>
              <p className="usage eng">
                <span className="used">NNN</span>/
                <span className="total">2GB</span>
              </p>
            </div>
            <div className="bar-box">
              <div className="fill-bar"></div>
            </div>
          </div>
        </div>
        <div className="project-list-container">
          <p className="project-counter eng">3 / 3</p>
          <div className="project-list-box">
            <div className="project-box eng">
              <span className="git-repository">GitHubId/RepositoryName</span>
              <span className="status active"></span>
              <p className="project-title">Project Name</p>
              <p className="project-url">subdomain.q-wik.com</p>
              <p className="version">
                ver. <span>COMMIN MESSAGE</span>
              </p>
              <div className="date-box">
                <p className="origin">
                  최초 <span>yy.mm.dd</span>
                </p>
                <span>/</span>
                <p className="update">
                  마지막 <span>yy.mm.dd hh:mm</span>
                </p>
              </div>
            </div>
            <div className="project-box eng">
              <span className="git-repository">GitHubId/RepositoryName</span>
              <span className="status inactive"></span>
              <p className="project-title">Project Name</p>
              <p className="project-url">subdomain.q-wik.com</p>
              <p className="version">
                ver. <span>COMMIN MESSAGE testtesttesttest</span>
              </p>
              <div className="date-box">
                <p className="origin">
                  최초 <span>yy.mm.dd</span>
                </p>
                <span>{}/</span>
                <p className="update">
                  마지막 <span>yy.mm.dd hh:mm</span>
                </p>
              </div>
            </div>
            <div className="project-box eng">
              <span className="git-repository">GitHubId/RepositoryName</span>
              <span className="status active"></span>
              <p className="project-title">Project Name</p>
              <p className="project-url">subdomain.q-wik.com</p>
              <p className="version">
                ver. <span>COMMIN MESSAGE</span>
              </p>
              <div className="date-box">
                <p className="origin">
                  최초 <span>yy.mm.dd</span>
                </p>
                <span>/</span>
                <p className="update">
                  마지막 <span>yy.mm.dd hh:mm</span>
                </p>
              </div>
            </div>
            <div className="project-box eng full">
              <i className="fas fa-plus"></i>
              <p>프로젝트를 더 배포하고 싶다면?</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Dashboard;
