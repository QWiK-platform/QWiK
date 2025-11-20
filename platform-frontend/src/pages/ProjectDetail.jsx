import React from "react";
import "./ProjectDetail.css";

const ProjectDetail = () => {
  return (
    <section className="project-detail-section">
      <div className="wrap">
        <div className="project-info-container">
          <p className="title">Project Name</p>
          <div className="toggle-box inactive">
            <span className="toggle"></span>
          </div>
          <div className="subdomain-box">
            <a
              href="#"
              target="_blank"
              rel="noopener noreferrer"
              className="project-url eng"
            >
              subdomain.qwik.com
            </a>
            <button className="change-subdomain-btn">변경하기</button>
          </div>
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
        <div className="history-container">
          <p className="title">배포 히스토리</p>
          <div className="history-box">
            <p>
              <span className="eng">yy.mm.dd hh:mm</span> commit message
            </p>
            <p>
              <span className="eng">yy.mm.dd hh:mm</span> 어느길이까지 가능한지
              테스트 작업 말줄임표 나올 때까지 길어지게 입력
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ProjectDetail;
