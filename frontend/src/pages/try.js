import React from 'react';
import Layout from '@theme/Layout';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

const ComingSoonPage = () => {
  const { siteConfig } = useDocusaurusContext();

  return (
    <Layout
      title="Coming Soon"
      description="Our site is coming soon!"
    >
      <main className="coming-soon-container">
        <div className="content">
          <h1 className='txtColor'>Coming Soon</h1>
          <p className='txtColor'>We're working hard to bring you something amazing. Stay tuned!</p>
          <div className="cta-buttons">
            <a href="https://github.com/rohnsha0/SwasthAI" target='_blank' rel="noopener noreferrer" className="button primary" aria-label="Visit Github Repository">Visit Github Repository</a>
          </div>
        </div>
      </main>
      <style jsx>{`
        .txtColor {
            color: var(--ifm-font-color-base);
        }

        .coming-soon-container {
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          min-height: 100vh;
          background: linear-gradient(to bottom, --ifm-color-primary-lightest, --ifm-color-primary);
          color: #333;
          padding: 1rem;
          text-align: center;
        }

        .content {
          max-width: 600px;
        }

        h1 {
          color: --ifm-color-primary
        }

        h2 {
          font-size: 2rem;
          margin-bottom: 1.5rem;
        }

        p {
          font-size: 1.2rem;
          margin-bottom: 2rem;
        }

        .clock-icon {
          width: 64px;
          height: 64px;
          margin-bottom: 2rem;
          color: var(--ifm-color-primary);
        }

        .cta-buttons {
          display: flex;
          justify-content: center;
          gap: 1rem;
        }

        .button {
          display: inline-block;
          padding: 0.75rem 1.5rem;
          border-radius: 9999px;
          text-decoration: none;
          font-weight: bold;
          transition: background-color 0.3s ease;
        }

        .primary {
          background-color: var(--ifm-color-primary);
          color: white;
        }

        .primary:hover {
          background-color: var(--ifm-color-primary-dark);
        }

        .secondary {
          background-color: white;
          color: var(--ifm-color-primary);
        }

        .secondary:hover {
          background-color: var(--ifm-color-primary-lightest);
        }
      `}</style>
    </Layout>
  );
};

export default ComingSoonPage;
