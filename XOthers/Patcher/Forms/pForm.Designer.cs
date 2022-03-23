namespace Sanchez.Patcher
{
    partial class pForm
    {
        private System.ComponentModel.IContainer components = null;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }

            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code
        private void InitializeComponent()
        {
            this.statusStrip = new System.Windows.Forms.StatusStrip();
            this.Status = new System.Windows.Forms.ToolStripStatusLabel();
            this.completeProgress = new System.Windows.Forms.ProgressBar();
            this.currentProgress = new System.Windows.Forms.ProgressBar();
            this.completeProgressText = new System.Windows.Forms.Label();
            this.currentProgressText = new System.Windows.Forms.Label();
            this.Start = new System.Windows.Forms.Button();
            this.StartCFG = new System.Windows.Forms.Button();
            this.statusStrip.SuspendLayout();
            this.SuspendLayout();
            // 
            // statusStrip
            // 
            this.statusStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.Status});
            this.statusStrip.Location = new System.Drawing.Point(0, 439);
            this.statusStrip.Name = "statusStrip";
            this.statusStrip.Size = new System.Drawing.Size(784, 22);
            this.statusStrip.TabIndex = 0;
            this.statusStrip.Text = "Status";
            // 
            // Status
            // 
            this.Status.Name = "Status";
            this.Status.Size = new System.Drawing.Size(0, 17);
            // 
            // completeProgress
            // 
            this.completeProgress.Location = new System.Drawing.Point(0, 363);
            this.completeProgress.Name = "completeProgress";
            this.completeProgress.Size = new System.Drawing.Size(784, 21);
            this.completeProgress.TabIndex = 1;
            // 
            // currentProgress
            // 
            this.currentProgress.Location = new System.Drawing.Point(0, 415);
            this.currentProgress.Name = "currentProgress";
            this.currentProgress.Size = new System.Drawing.Size(784, 21);
            this.currentProgress.TabIndex = 2;
            // 
            // completeProgressText
            // 
            this.completeProgressText.AutoSize = true;
            this.completeProgressText.BackColor = System.Drawing.Color.Transparent;
            this.completeProgressText.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.completeProgressText.ForeColor = System.Drawing.SystemColors.ControlLight;
            this.completeProgressText.Location = new System.Drawing.Point(-5, 335);
            this.completeProgressText.Name = "completeProgressText";
            this.completeProgressText.Size = new System.Drawing.Size(202, 25);
            this.completeProgressText.TabIndex = 3;
            this.completeProgressText.Text = "Postup stahování: 0%";
            // 
            // currentProgressText
            // 
            this.currentProgressText.AutoSize = true;
            this.currentProgressText.BackColor = System.Drawing.Color.Transparent;
            this.currentProgressText.Cursor = System.Windows.Forms.Cursors.No;
            this.currentProgressText.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.currentProgressText.ForeColor = System.Drawing.SystemColors.ControlLight;
            this.currentProgressText.Location = new System.Drawing.Point(-5, 387);
            this.currentProgressText.Name = "currentProgressText";
            this.currentProgressText.Size = new System.Drawing.Size(292, 25);
            this.currentProgressText.TabIndex = 4;
            this.currentProgressText.Text = "Aktuální soubor: 0%  |  0.00 kb/s";
            // 
            // Start
            // 
            this.Start.Enabled = false;
            this.Start.Location = new System.Drawing.Point(0, 1);
            this.Start.Name = "Start";
            this.Start.Size = new System.Drawing.Size(197, 40);
            this.Start.TabIndex = 5;
            this.Start.Text = "Spustit hru";
            this.Start.UseVisualStyleBackColor = true;
            this.Start.Click += new System.EventHandler(this.Start_Click);
            // 
            // StartCFG
            // 
            this.StartCFG.Enabled = false;
            this.StartCFG.Location = new System.Drawing.Point(668, 1);
            this.StartCFG.Name = "StartCFG";
            this.StartCFG.Size = new System.Drawing.Size(116, 40);
            this.StartCFG.TabIndex = 6;
            this.StartCFG.Text = "Nastavení";
            this.StartCFG.UseVisualStyleBackColor = true;
            this.StartCFG.Click += new System.EventHandler(this.StartCFG_Click);
            // 
            // pForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ControlDarkDark;
            this.ClientSize = new System.Drawing.Size(784, 461);
            this.Controls.Add(this.StartCFG);
            this.Controls.Add(this.Start);
            this.Controls.Add(this.currentProgressText);
            this.Controls.Add(this.completeProgressText);
            this.Controls.Add(this.currentProgress);
            this.Controls.Add(this.completeProgress);
            this.Controls.Add(this.statusStrip);
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(800, 500);
            this.MinimumSize = new System.Drawing.Size(800, 500);
            this.Name = "pForm";
            this.ShowIcon = false;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Lorderon patcher";
            this.Shown += new System.EventHandler(this.pForm_Shown);
            this.statusStrip.ResumeLayout(false);
            this.statusStrip.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.StatusStrip statusStrip;
        public  System.Windows.Forms.ToolStripStatusLabel Status;
        public  System.Windows.Forms.ProgressBar completeProgress;
        public  System.Windows.Forms.ProgressBar currentProgress;
        public  System.Windows.Forms.Label completeProgressText;
        public  System.Windows.Forms.Label currentProgressText;
        public  System.Windows.Forms.Button Start;
        public System.Windows.Forms.Button StartCFG;
    }
}

